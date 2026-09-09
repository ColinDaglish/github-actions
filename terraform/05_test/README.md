# Test Terraform Configuration

This directory contains minimal, valid Terraform configuration files used for testing the `terraform-quality` GitHub Actions workflow.

## Files

- `terraform.tf` - Terraform version and provider requirements
- `main.tf` - A simple null resource for testing
- `variables.tf` - Test input variables
- `outputs.tf` - Test outputs

## Purpose

These files are designed to:
- Pass `terraform fmt` validation
- Pass `terraform validate` validation  
- Pass `tflint` linting checks
- Serve as test artifacts for the GitHub Actions workflow tests

Do not modify these files unless you're updating the test suite.
