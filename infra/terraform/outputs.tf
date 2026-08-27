output "cloud_run_service_uri" {
  description = "The internal URI of the deployed Cloud Run Regulatory Agent."
  value       = google_cloud_run_v2_service.agent_service.uri
}

output "service_account_email" {
  description = "Service account email executing the agent."
  value       = google_service_account.agent_sa.email
}
