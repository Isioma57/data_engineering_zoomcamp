# Terraform

## Definition

Terraform is an Infrastructure as Code(Iac) tool that lets you define both cloud and on-prem resources in human readable configuration files that you can version, reuse and share.

Terraform generates an execution plan that will show you what it will do when you call `terraform apply`. It gives you a chance to review before it makes any changes to your infrastructure. 

## Why Terraform

Simplicity in keeping track of infrastructure

Easier Collaboration

Reproducibility

Ensure resources are removed

## Key Terraform Commands

### Init
The terraform init command is used to initialize a Terraform working directory, setting up everything needed for Terraform to run. It installs the necessary providers, initializes backends for state management, and prepares the environment for other commands like plan and apply.

### Plan
terraform plan creates an execution plan, showing what actions Terraform will take to change the infrastructure to match the configuration. It's a crucial step for reviewing changes before they are applied, ensuring that the actions Terraform will perform are expected and safe.

### Apply
The terraform apply command is used to apply the changes required to reach the desired state of the configuration. It will execute the actions proposed in the terraform plan step, modifying the infrastructure as needed to match the Terraform configuration files.

### Destroy
terraform destroy is the command for removing all the resources defined in the Terraform configuration. This command is used to tear down the infrastructure managed by Terraform, which is useful for cleaning up resources that are no longer needed.
