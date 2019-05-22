terragrunt = {
  remote_state {
    backend = "s3"
    config {
      bucket         = "natali-terraform-state"
      key            = "${path_relative_to_include()}/terraform.tfstate"
      region         = "eu-west-1"
      encrypt        = true

      s3_bucket_tags {
        owner = "terragrunt integration test"
        name  = "Terraform state storage"
      }
    }
  }

  terraform {
    source = "github.com/rafaelmnatali/terraform_modules/core/network"
  }
}

aws_region = "eu-west-1"
cidr_block = "10.132.0.0/16"