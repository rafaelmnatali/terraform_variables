terragrunt = {
  terraform {
    source = "github.com/rafaelmnatali/terraform_modules/core/network"
  }
}

aws_region = "eu-west-1"
cidr_block = "10.132.0.0/16"