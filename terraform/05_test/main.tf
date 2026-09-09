# Test terraform configuration for GitHub Actions workflow validation
# This is a minimal valid terraform configuration used for testing

resource "null_resource" "test_artifact" {
  triggers = {
    test_name = var.test_name
  }

  provisioner "local-exec" {
    command = "echo 'Test artifact for terraform quality checks'"
  }
}
