up-dev:
	-terraform init
	-terraform workspace new dev
	-terraform workspace select dev
	-terraform apply -var-file="unsafe.tfvars" -var-file="safe-dev.json"

plan-dev:
	-terraform init
	-terraform workspace new dev
	-terraform workspace select dev
	-terraform plan -var-file="unsafe.tfvars" -var-file="safe-dev.json"

down-dev:
	-terraform init
	-terraform workspace new dev
	-terraform workspace select dev
	-terraform destroy -var-file="unsafe.tfvars" -var-file="safe-dev.json"

#	-		-		-

up-staging:
	-terragrunt init
	-terragrunt workspace new staging
	-terragrunt workspace select staging
	-terragrunt plan -var-file="./stage/core/network/terraform.tfvars"
	#-terraform apply -var-file="unsafe.tfvars" -var-file="safe-staging.json"

plan-staging:
	-terraform init
	-terraform workspace new staging
	-terraform workspace select staging
	-terraform plan -var-file="unsafe.tfvars" -var-file="safe-staging.json"

down-staging:
	-terraform init
	-terraform workspace new staging
	-terraform workspace select staging
	-terraform destroy -var-file="unsafe.tfvars" -var-file="safe-staging.json"

#	-		-		-

up-production:
	-terraform init
	-terraform workspace new production
	-terraform workspace select production
	-terraform apply -var-file="unsafe.tfvars" -var-file="safe-production.json"

plan-production:
	-terraform init
	-terraform workspace new production
	-terraform workspace select production
	-terraform plan -var-file="unsafe.tfvars" -var-file="safe-production.json"

down-production:
	-terraform init
	-terraform workspace new production
	-terraform workspace select production
	-terraform destroy -var-file="unsafe.tfvars" -var-file="safe-production.json"