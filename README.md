1. Azure VM Deployment Automation Flow:

Azure Virtual Machine Deployment:
   File for Deployment:
      main.tf
      outputs.tf
      providers.tf
      ssh.tf
      variables.tf
       
Execution of the Terraform Script:
   Go to GitHub Actions
   Select the "Create the Azure VM Instance" workflow.
   Click Runflow
   Run workflow

Workflow will automatically execute the scripts:

main.tf configuration:
   azurerm_virtual_network -> 
      name                = "myVnet"
      address_space       = ["10.0.0.0/16"]
      location            = azurerm_resource_group.rg.location
      resource_group_name = azurerm_resource_group.rg.name
      
azurerm_subnet ->
   name                 = "mySubnet"
   resource_group_name  = azurerm_resource_group.rg.name
   virtual_network_name = azurerm_virtual_network.my_terraform_network.name
   address_prefixes     = ["10.0.1.0/24"]
     Security Rule ->
        security_rule {
           name                       = "SSH"
           priority                   = 1000
           direction                  = "Inbound"
           access                     = "Allow"
           protocol                   = "Tcp"
           source_port_range          = "*"
           destination_port_range     = "22"
           source_address_prefix      = "*"
           destination_address_prefix = "*"
         }
         security_rule {
           name                       = "Web"
           priority                   = 1001
           direction                  = "Inbound"
           access                     = "Allow"
           protocol                   = "Tcp"
           source_port_range          = "*"
           destination_port_range     = "80"
           source_address_prefix      = "*"
           destination_address_prefix = "*"
         }

Username and Password:
   computer_name  = "hostname"
   admin_username = var.username
   admin_password = "Dbs@1234567"
   disable_password_authentication = false

Configure the above configuration inside the Terraform -> main.tf file.

Process: 
  
  Github Actions -> Click on Azure VM Instance -> Run Workflow -> Click on workflow execute.
  Wait for about 5-6 min for the deployment process.
  Then go to the Github Action Task
  In the terminal, you will find the IP address for the Azure VM.

![image](https://github.com/user-attachments/assets/b374307d-facd-4eee-873c-2965b2c3295b)

  
![image](https://github.com/user-attachments/assets/66f9c434-9527-4dca-abdc-3b84c6b436fc)

![image](https://github.com/user-attachments/assets/9fe0594f-c5c8-4ad0-89a7-7cfb6c97f5c5)


![image](https://github.com/user-attachments/assets/b8b69210-4293-44c4-a130-d13311f8d5e4)


2. Automated CI CD Deployment:
 
   When a developer pushes thier code to main branch, the CI CD Pipeline will be triggered automatically.
   
   The Ansible playbook will execute the following instructions:
      Install Docker
      Load the Docker Image
      Create and Run the container
      Clean the old Docker Image .tar files.
   
   Output:
     ![image](https://github.com/user-attachments/assets/3d4fcb1a-23cb-4683-8185-cc648ea2a1b3)

This image show the final output of the application deployment.

![image](https://github.com/user-attachments/assets/ff98ab10-5b39-455c-a568-10d24343d5a2)


        


