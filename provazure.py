import os.path
import sys
from deployer import Deployer

# {
#     "cloudName": "AzureCloud",
#     "id": "4e47036e-f8d5-43a7-8fa8-ca7d32a44fab",
#     "isDefault": true,
#     "name": "Azure Free Trial",
#     "state": "Enabled",
#     "tenantId": "d598d3d6-a9ea-42cb-8441-a73d7ef1006b",
#     "user": {
#         "name": "antoine.legall@guillaumemorelinvivoo.onmicrosoft.com",
#         "type": "user"
#     }
# }

# os.environ['AZURE_TENANT_ID'] = "d598d3d6-a9ea-42cb-8441-a73d7ef1006b" # with your Azure Active Directory tenant id or domain
# os.environ['AZURE_SUBSCRIPTION_ID'] = "4e47036e-f8d5-43a7-8fa8-ca7d32a44fab" # with your Azure Active Directory Application Secret
# os.environ['AZURE_CLIENT_ID'] = "antoine.legall@guillaumemorelinvivoo.onmicrosoft.com" # with your Azure Active Directory Application Client ID
# # os.environ['AZURE_CLIENT_ID'] = "6724ac8f-2d97-463e-9f58-c6915afc29a2" # with your Azure Active Directory Application Client ID
# # os.environ['AZURE_CLIENT_SECRET'] = "Norm@nd567" # with your Azure Active Directory Application Secret
# os.environ['AZURE_CLIENT_SECRET'] = "Norm@nd567" # with your Azure Active Directory Application Secret

# my_subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID', '11111111-1111-1111-1111-111111111111')   # your Azure Subscription Id

# my_pub_ssh_key_path = os.path.expanduser('~/.ssh/id_rsa.pub')   # the path to your rsa public key file

# msg = "\nInitializing the Deployer class with subscription id: {}, resource group: {}" \
#     "\nand public key located at: {}...\n\n"
# msg = msg.format(my_subscription_id, my_resource_group, my_pub_ssh_key_path)
# print(msg)

# print("Deployment set with "+my_subscription_id+" and "+my_resource_group)

# sys.exit(0)

# Standard_A0,Standard_A1,Standard_A2,Standard_A3,Standard_A5,Standard_A4,Standard_A6,Standard_A7,Basic_A0,Basic_A1,Basic_A2,Basic_A3,Basic_A4,Standard_D1
# Standard_D2,Standard_D3,Standard_D4,Standard_D11,Standard_D12,Standard_D13,Standard_D14,Standard_A1_v2,Standard_A2m_v2,Standard_A2_v2,Standard_A4m_v2,Standard_A4_v2
# Standard_A8m_v2,Standard_A8_v2,Standard_DS1,Standard_DS2,Standard_DS3,Standard_DS4,Standard_DS11,Standard_DS12,Standard_DS13,Standard_DS14,Standard_D1_v2,Standard_D2_v2
# Standard_D3_v2,Standard_D4_v2,Standard_D5_v2,Standard_D11_v2,Standard_D12_v2,Standard_D13_v2,Standard_D14_v2,Standard_D15_v2,Standard_D2_v2_Promo,Standard_D3_v2_Promo
# Standard_D4_v2_Promo,Standard_D5_v2_Promo,Standard_D11_v2_Promo,Standard_D12_v2_Promo,Standard_D13_v2_Promo,Standard_D14_v2_Promo,Standard_F1,Standard_F2,Standard_F4,Standard_F8
# Standard_F16,Standard_B1ms,Standard_B1s,Standard_B2ms,Standard_B2s,Standard_B4ms,Standard_B8ms,Standard_DS1_v2,Standard_DS2_v2,Standard_DS3_v2,Standard_DS4_v2,Standard_DS5_v2
# Standard_DS11_v2,Standard_DS12_v2,Standard_DS13-2_v2,Standard_DS13-4_v2,Standard_DS13_v2,Standard_DS14-4_v2,Standard_DS14-8_v2,Standard_DS14_v2,Standard_DS15_v2,Standard_DS2_v2_Promo
# Standard_DS3_v2_Promo,Standard_DS4_v2_Promo,Standard_DS5_v2_Promo,Standard_DS11_v2_Promo,Standard_DS12_v2_Promo,Standard_DS13_v2_Promo,Standard_DS14_v2_Promo,Standard_F1s,Standard_F2s
# Standard_F4s,Standard_F8s,Standard_F16s,Standard_D2_v3,Standard_D4_v3,Standard_D8_v3,Standard_D16_v3,Standard_D32_v3,Standard_D2s_v3,Standard_D4s_v3,Standard_D8s_v3,Standard_D16s_v3
# Standard_D32s_v3,Standard_NV6,Standard_NV12,Standard_NV24,Standard_D64_v3,Standard_D64s_v3,Standard_E2_v3,Standard_E4_v3,Standard_E8_v3,Standard_E16_v3,Standard_E32_v3,Standard_E64_v3
# Standard_E2s_v3,Standard_E4s_v3,Standard_E8s_v3,Standard_E16s_v3,Standard_E32s_v3,Standard_E64s_v3,Standard_F2s_v2,Standard_F4s_v2,Standard_F8s_v2,Standard_F16s_v2,Standard_F32s_v2
# Standard_F64s_v2,Standard_F72s_v2,Standard_NC6,Standard_NC12,Standard_NC24,Standard_NC24r,Standard_H8,Standard_H16,Standard_H8m,Standard_H16m,Standard_H16r,Standard_H16mr,Standard_G1
# Standard_G2,Standard_G3,Standard_G4,Standard_G5,Standard_GS1,Standard_GS2,Standard_GS3,Standard_GS4,Standard_GS4-4,Standard_GS4-8,Standard_GS5,Standard_GS5-8,Standard_GS5-16
# Standard_L4s,Standard_L8s,Standard_L16s,Standard_L32s,Standard_M64-16ms,Standard_M64-32ms,Standard_M64ms,Standard_M64s,Standard_M128-32ms,Standard_M128-64ms,Standard_M128ms
# Standard_M128s,Standard_ND6s,Standard_ND12s,Standard_ND24rs,Standard_ND24s,Standard_E32-8s_v3,Standard_E32-16s_v3,Standard_E64-16s_v3,Standard_E64-32s_v3,Standard_NC6s_v2
# Standard_NC12s_v2,Standard_NC24rs_v2,Standard_NC24s_v2,Standard_A8,Standard_A9,Standard_A10,Standard_A11

user="antoine.legall@guillaumemorelinvivoo.onmicrosoft.com"
passwd="Norm@nd567"
my_subscription_id="4e47036e-f8d5-43a7-8fa8-ca7d32a44fab"
my_resource_group = 'Invivoo-elastic'

# Initialize the deployer class
# deployer = Deployer(my_subscription_id, my_resource_group, my_pub_ssh_key_path)
print("Deployment set with "+my_subscription_id+" and "+my_resource_group)
deployer = Deployer(user, passwd, my_subscription_id, my_resource_group)

# Deploy the template
print("Beginning the deployment... \n\n")
my_deployment = deployer.deploy()

print("Done deploying !!\n\nYou can connect via: `ssh azureSample@{}.westeuropo.cloudapp.azure.com`".format(deployer.dns_label_prefix))

# Destroy the resource group which contains the deployment
# deployer.destroy()