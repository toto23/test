import os.path
import json
from haikunator import Haikunator
from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import DeploymentMode

class Deployer(object):
    """ Initialize the deployer class with subscription, resource group and public key.
    :raises IOError: If the public key path cannot be read (access or not exists)
    :raises KeyError: If AZURE_CLIENT_ID, AZURE_CLIENT_SECRET or AZURE_TENANT_ID env
        variables or not defined
    """
    name_generator = Haikunator()

    def __init__(self, user, passwd, subscription_id, resource_group):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.dns_label_prefix = self.name_generator.haikunate()
        self.credentials = UserPassCredentials(user, passwd)
        self.client = ResourceManagementClient(self.credentials, self.subscription_id)

    def deploy(self):
        """Deploy the template to a resource group."""

        self.client.resource_groups.create_or_update(
            self.resource_group,
            {
                'location':'westeurope'
            }
        )

        template_path = os.path.join(os.path.dirname(__file__), 'config', 'azuredeploy.json')
        with open(template_path, 'r') as tpl_file:
            template = json.load(tpl_file)
        tpl_file.close()

        # parameters_path = os.path.join(os.path.dirname(__file__), 'config', 'azuredeploy.parameters.json')
        # with open(parameters_path, 'r') as param_file:
        #     # params = json.load(param_file)
        #     params = json.loads(param_file)
        # param_file.close()

        params = {
            'adminUsername': '',
            'adminPassword': '',
            'vmName': 'elastic'
        }
        params = {k: {'value': v} for k, v in params.items()}

        # params must be a dictionnary
        deployment_properties = {
            'mode': DeploymentMode.incremental,
            'template': template,
            'parameters': params
        }

        deployment_async_operation = self.client.deployments.create_or_update(
            self.resource_group,
            'Invivoo-elastic-deployment',
            deployment_properties
        )
        deployment_async_operation.wait()

    def destroy(self):
        """Destroy the given resource group"""
        self.client.resource_groups.delete(self.resource_group)