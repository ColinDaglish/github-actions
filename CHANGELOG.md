# Changelog

## [1.6.0](https://github.com/datasciencecampus/github-actions/compare/v1.5.0...v1.6.0) (2026-09-09)


### Features

* add continue_on_error input for negative testing in Terraform quality workflow ([c58dc70](https://github.com/datasciencecampus/github-actions/commit/c58dc705d7eeb1bfd2a1db0e441774fd1c0a613d))
* add continue-on-error option for terraform-dirs validation step ([05c2c29](https://github.com/datasciencecampus/github-actions/commit/05c2c29a2b4e8395d8f34e17239cd3fbe0ea0638))
* add minimal Terraform configurations for sandbox, dev nonprod, stg prod, and prd prod environments ([af5b009](https://github.com/datasciencecampus/github-actions/commit/af5b0093701dfd17747b35fc0bbec0f50c4b7d23))
* add reusable Terraform quality testing workflow with positive and negative test cases ([0b7f306](https://github.com/datasciencecampus/github-actions/commit/0b7f3060870d20676ec923df828b053d98426674))
* add Terraform quality workflow with validation, formatting, and linting steps ([67063f0](https://github.com/datasciencecampus/github-actions/commit/67063f05fd7c1cdb1a9bd0a261ac0309737f1301))
* add terraform-quality checks ([26dbbdc](https://github.com/datasciencecampus/github-actions/commit/26dbbdcaced032e26196237f659bee8924939339))
* add TFLint configuration for AWS, Google, and Azure plugins with rules enabled ([2aa990b](https://github.com/datasciencecampus/github-actions/commit/2aa990b28bb82352934b323d27cfba89de8851ca))
* add validation outputs for terraform-dirs and enhance test reporting ([983b562](https://github.com/datasciencecampus/github-actions/commit/983b5625a127c7276c72eb534e606896ef7d41ba))
* enhance validation logic for Terraform quality checks with continue-on-error option ([08e9511](https://github.com/datasciencecampus/github-actions/commit/08e95115b40ef9a88d50903b2302da4fc1d5ab30))
* organize test groups and update terraform version for quality checks ([d687a31](https://github.com/datasciencecampus/github-actions/commit/d687a3114dd3de7932fc0949c6bfb4f2ae09c89f))
* specify terraform directories for positive tests in reusable workflow ([07c5b02](https://github.com/datasciencecampus/github-actions/commit/07c5b0242907c5b8c30445f2bb36c30da4876db5))
* update positive test for specific terraform directory and enable formatting check ([7c85323](https://github.com/datasciencecampus/github-actions/commit/7c853230af44a3f93e039e742d5300abb502aec1))
* update positive test to use 'terraform/05_test' directory ([c88c164](https://github.com/datasciencecampus/github-actions/commit/c88c1647d7172e5d46467f23e81e41e177972667))


### Bug Fixes

* adjust arguments for better performance. ([6ebb3e3](https://github.com/datasciencecampus/github-actions/commit/6ebb3e3fe8603d672aa03169376d69586ed31fb3))
* correct failure conditions for negative tests in Terraform quality checks ([165fb05](https://github.com/datasciencecampus/github-actions/commit/165fb05f02c670368494fb2f8551789b9c20525f))
* ensure negative test cases continue on error for better workflow resilience ([f395e03](https://github.com/datasciencecampus/github-actions/commit/f395e03431eb0634d3bd8f219ad8a12d8b77c354))
* improve failure conditions for negative tests in Terraform quality checks ([4022eb1](https://github.com/datasciencecampus/github-actions/commit/4022eb157feba8947e1a8a8c7ddc29f39ce7f3fa))
* update positive test references to use test directory instead of all directories ([155ad48](https://github.com/datasciencecampus/github-actions/commit/155ad48d4f1bf7faf8ffd0eb12ffef7ac1db443a))
* update tflint setup action to version 6.3.1 for improved linting capabilities ([73deef2](https://github.com/datasciencecampus/github-actions/commit/73deef260ef518d4dccf4a86c67345c33a5c07df))
* use bracket notation for terraform version ([838450a](https://github.com/datasciencecampus/github-actions/commit/838450aa7cc6c8816453f97ddb9aaf9319a1b503))

## [1.5.0](https://github.com/datasciencecampus/github-actions/compare/v1.4.0...v1.5.0) (2026-08-25)


### Features

* enhance issue and pull request reusable workflows with automatic field value derivation and improved documentation ([1eee193](https://github.com/datasciencecampus/github-actions/commit/1eee19379097778e78cd81d624d2a6f17f117fd4))
* enhance workflow configurations with concurrency settings and improved job names ([2d7d036](https://github.com/datasciencecampus/github-actions/commit/2d7d036f044f94a683313ac2d28257d310582330))

## [1.4.0](https://github.com/datasciencecampus/github-actions/compare/v1.3.0...v1.4.0) (2026-08-25)


### Features

* add Code of Conduct, Security Notice, and contributing guidelines ([bd714e8](https://github.com/datasciencecampus/github-actions/commit/bd714e8eb84a713b7b1fe2708c572705e7033bf5))

## [1.3.0](https://github.com/datasciencecampus/github-actions/compare/v1.2.2...v1.3.0) (2026-08-25)


### Features

* add pull request template for improved contribution guidelines ([ec0e6e1](https://github.com/datasciencecampus/github-actions/commit/ec0e6e13bf5c0f7b0650b17244eae85bd7309620))

## [1.2.2](https://github.com/datasciencecampus/github-actions/compare/v1.2.1...v1.2.2) (2026-08-24)


### Bug Fixes

* require project_field_values and node_id for manual tests in reusable workflows ([f3171c7](https://github.com/datasciencecampus/github-actions/commit/f3171c7064075cc9456f1aabbeeb9d298cab3041))
* update project_field_values examples to use project ID 1234 ([4b8471e](https://github.com/datasciencecampus/github-actions/commit/4b8471ebc26552f882b10df4f40e6b59b1a8ee88))

## [1.2.1](https://github.com/datasciencecampus/github-actions/compare/v1.2.0...v1.2.1) (2026-08-24)


### Bug Fixes

* update implementation reference handling in workflows and documentation ([d664403](https://github.com/datasciencecampus/github-actions/commit/d664403ed3b78a4d8ae3ab67d90bebaf38cc8041))

## [1.2.0](https://github.com/datasciencecampus/github-actions/compare/v1.1.0...v1.2.0) (2026-08-24)


### Features

* enhance reusable workflows with implementation reference resolution and update documentation ([d1794d9](https://github.com/datasciencecampus/github-actions/commit/d1794d9e2c379286f26a4cb1e368bfe1c9a3f97b))

## [1.1.0](https://github.com/datasciencecampus/github-actions/compare/v1.0.1...v1.1.0) (2026-08-24)


### Features

* **workflows:** add implementation_ref input to issue and PR workflows for internal dispatching ([eca7810](https://github.com/datasciencecampus/github-actions/commit/eca78105ae82edf65a71f317e1ee25be601bc528))

## [1.0.1](https://github.com/datasciencecampus/github-actions/compare/v1.0.0...v1.0.1) (2026-08-24)


### Bug Fixes

* **workflows:** add PULL_REQUEST_HEAD_REF to validate dispatch inputs for pull requests ([25926fa](https://github.com/datasciencecampus/github-actions/commit/25926fa9c904d46969dd2885d042ffe24970dc92))

## [1.0.0](https://github.com/datasciencecampus/github-actions/compare/v0.2.0...v1.0.0) (2026-08-24)


### ⚠ BREAKING CHANGES

* **workflows:** callers must use add-issue-to-projects.yml and add-pr-to-projects.yml; the legacy call-add-* workflow files were removed.

### Code Refactoring

* **workflows:** Refactor GitHub Actions workflows for adding issues and pull requests to projects ([4436eb1](https://github.com/datasciencecampus/github-actions/commit/4436eb1c2ee7a983b04e8e1cfa9d1c5ee746b03f))

## [0.2.0](https://github.com/datasciencecampus/github-actions/compare/v0.1.0...v0.2.0) (2026-08-24)


### Features

* Add Dependabot configuration for GitHub Actions version updates ([638f9b9](https://github.com/datasciencecampus/github-actions/commit/638f9b9beca251baf439ea3b5d683312a0cf4d9f))
* Add initial documentation structure with sections for tutorials, how-to guides, reference, and explanations ([4f91558](https://github.com/datasciencecampus/github-actions/commit/4f915589e0969be3464eb4b4da7afb447a319318))
* Add initial Zizmor workflow and default configuration file for GitHub Actions security analysis ([8ca5f40](https://github.com/datasciencecampus/github-actions/commit/8ca5f40e9751ff6fbc593d41503a358665fd801a))
* Add release-please workflow and configuration for automated releases ([8f85b8c](https://github.com/datasciencecampus/github-actions/commit/8f85b8c166fcc4a8000fefc957f122be27d43743))
* Add request form for GitHub token access and enhance project-routing workflows with validation checks ([aa31035](https://github.com/datasciencecampus/github-actions/commit/aa3103552d8d2becfe55ad9bb4a5263ee7a1dc97))
* Add reusable workflow for adding issues to projects and update README ([14c86c5](https://github.com/datasciencecampus/github-actions/commit/14c86c591b6a500abb17842b11afa3fe11d8488b))
* Add validation action for project handler app credentials and update workflows to use it ([82bb466](https://github.com/datasciencecampus/github-actions/commit/82bb466bcb23ec17f59b05cc05e6a83d653f2799))
* Add workflow for testing pull requests with project field mappings ([b742c1d](https://github.com/datasciencecampus/github-actions/commit/b742c1dcb94544fca6055d77d7fd7fc41df1b62e))
* Add workflow to add pull requests to projects with field value mappings ([1545e47](https://github.com/datasciencecampus/github-actions/commit/1545e4730987464a43f808f37f7fc5b5e0ae64fd))
* Add workflow to post reviewer instructions on access request issues ([5366d90](https://github.com/datasciencecampus/github-actions/commit/5366d90da9d60815db0869d917187396dc66dd96))
* Add workflow to update project routing allowlist based on closed issues ([9b3dc34](https://github.com/datasciencecampus/github-actions/commit/9b3dc34e2290fee8135b6b68a8db8bf2da940474))
* Add Zizmor workflow and update README to reflect repository name ([34391f7](https://github.com/datasciencecampus/github-actions/commit/34391f7ecddba932bb5f23cd44e69780c62b85e3))


### Bug Fixes

* Add missing newline at end of README.md for proper formatting ([4d89704](https://github.com/datasciencecampus/github-actions/commit/4d89704866d35401ea469f90de7bd5959aeaec4d))
* Add missing permission-pull-requests to GitHub App token creation ([90de8ba](https://github.com/datasciencecampus/github-actions/commit/90de8bac7ff10bfa692889e4bd90cdee502ad3a1))
* Correct default rules structure in Zizmor configuration file ([02ab7f3](https://github.com/datasciencecampus/github-actions/commit/02ab7f364fd247fc827947bc28ad3210a447a955))
* Remove unnecessary permission-pull-requests from workflow ([7f22dc1](https://github.com/datasciencecampus/github-actions/commit/7f22dc1f6a618d88044f95a6c0f0f3c5daa5ea78))
* Update comment-on-access-request workflow to improve API request handling and clarify environment variables ([937bcba](https://github.com/datasciencecampus/github-actions/commit/937bcbac086c6a57f6c34e8fd09924fb02cb3425))
* Update curl command to include --fail-with-body for better error handling ([b74ac90](https://github.com/datasciencecampus/github-actions/commit/b74ac90866f7821098f90d2c14e5d800891a63c0))
* Update field value from "In review" to "Review" in workflows and documentation ([a5f3a13](https://github.com/datasciencecampus/github-actions/commit/a5f3a13b6d92f6eaf68d8dd77300d5c410c10266))
* Update request form for GitHub token access to clarify project routing requirements ([1515219](https://github.com/datasciencecampus/github-actions/commit/15152199bf0c934587eeee680a03823631df6beb))
