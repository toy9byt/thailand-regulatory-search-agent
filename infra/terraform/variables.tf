variable "project_id" {
  description = "The Google Cloud Project ID hosting the regulatory agent."
  type        = string
  default     = "your-gcp-project-id"
}

variable "region" {
  description = "Target Google Cloud region (default: asia-southeast1)."
  type        = string
  default     = "asia-southeast1"
}

variable "container_image" {
  description = "Container image URI for Cloud Run deployment."
  type        = string
  default     = "asia-southeast1-docker.pkg.dev/your-gcp-project-id/agents/thailand-regulatory-search-agent:latest"
}
