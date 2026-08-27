# ==============================================================================
# Terraform Infrastructure as Code (IaC) for Thailand Regulatory Agent
# Provisions Cloud Run Service, Secret Manager Secret, and IAM Bindings
# ==============================================================================

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# 1. Service Account for Regulatory Agent
resource "google_service_account" "agent_sa" {
  account_id   = "sa-thailand-regulatory-agent"
  display_name = "Thailand Regulatory Search Agent Service Account"
}

# 2. Secret Manager Secret for Gemini API Key / Credentials
resource "google_secret_manager_secret" "gemini_api_key" {
  secret_id = "thailand-regulatory-gemini-api-key"
  replication {
    auto {}
  }
}

# 3. IAM Secret Accessor Binding
resource "google_secret_manager_secret_iam_member" "sa_secret_access" {
  secret_id = google_secret_manager_secret.gemini_api_key.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.agent_sa.email}"
}

# 4. Cloud Trace Agent Role Binding
resource "google_project_iam_member" "trace_agent" {
  project = var.project_id
  role    = "roles/cloudtrace.agent"
  member  = "serviceAccount:${google_service_account.agent_sa.email}"
}

# 5. Cloud Run Service Deployment
resource "google_cloud_run_v2_service" "agent_service" {
  name     = "thailand-regulatory-search-agent"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER"

  template {
    service_account = google_service_account.agent_sa.email

    scaling {
      min_instance_count = 1
      max_instance_count = 10
    }

    containers {
      image = var.container_image

      resources {
        limits = {
          cpu    = "2"
          memory = "2Gi"
        }
      }

      env {
        name  = "GOOGLE_CLOUD_PROJECT"
        value = var.project_id
      }
      env {
        name  = "GOOGLE_CLOUD_LOCATION"
        value = var.region
      }
      env {
        name  = "TARGET_ENTITY_SCOPE"
        value = "PRIVATE_COMMERCIAL_BANK"
      }
      env {
        name  = "MODEL_ROUTING_STRATEGY"
        value = "PURE_FLASH_EXTENDED_THINKING"
      }
      env {
        name  = "THINKING_BUDGET"
        value = "4096"
      }

      env {
        name = "GEMINI_API_KEY"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.gemini_api_key.secret_id
            version = "latest"
          }
        }
      }
    }
  }
}
