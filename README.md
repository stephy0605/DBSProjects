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

  ![image](https://github.com/user-attachments/assets/ad28bc26-425d-4926-9072-fffee70481de)
  
  ![image](https://github.com/user-attachments/assets/5de4093b-2520-44b6-adf4-4b7a54868c68)

  ![image](https://github.com/user-attachments/assets/30197571-9d23-446c-94c0-78e206001979)

  ![image](https://github.com/user-attachments/assets/2dd42d35-ea78-4ae5-946b-a2155fb5c754)

  ![image](https://github.com/user-attachments/assets/96f1423e-ac51-47d2-a1d1-e06b9270cf49)


2. Automated CI CD Deployment:
 
   When a developer pushes thier code to main branch, the CI CD Pipeline will be triggered automatically.
   
   The Ansible playbook will execute the following instructions:
      Install Docker
      Load the Docker Image
      Create and Run the container
      Clean the old Docker Image .tar files.
   
   Output:
      - ![image](https://github.com/user-attachments/assets/ea92b455-33d7-4e03-b25d-74c558c67799)
      - ![image](https://github.com/user-attachments/assets/1fa27eee-f236-4f1a-941c-b9bcb60c0fa7)

This image show the final output of the application deployment.

![image](https://github.com/user-attachments/assets/5b3d7907-c29b-4bb2-939c-faeb4cf23060)

        


