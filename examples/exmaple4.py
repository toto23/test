def test_deployments(self):
    self.create_resource_group()

    # for more sample templates, see https://github.com/Azure/azure-quickstart-templates
    deployment_name = self.get_resource_name("pytestdeployment")

    deployment_exists = self.resource_client.deployments.check_existence(
        self.group_name,
        deployment_name
    )
    self.assertFalse(deployment_exists)

    template = {
        "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
            "location": {
                "type": "string",
                "allowedValues": [
                    "East US",
                    "West US",
                    "West Europe",
                    "East Asia",
                    "South East Asia"
                ],
                "metadata": {
                    "description": "Location to deploy to"
                }
            }
        },
        "resources": [
            {
                "type": "Microsoft.Compute/availabilitySets",
                "name": "availabilitySet1",
                "apiVersion": "2015-05-01-preview",
                "location": "[parameters('location')]",
                "properties": {}
            }
        ],
        "outputs": {
            "myparameter": {
                "type": "object",
                "value": "[reference('Microsoft.Compute/availabilitySets/availabilitySet1')]"
            }
        }
    }
    # Note: when specifying values for parameters, omit the outer elements
    parameters = {"location": {"value": "West US"}}
    deployment_params = azure.mgmt.resource.resources.models.DeploymentProperties(
        mode=azure.mgmt.resource.resources.models.DeploymentMode.incremental,
        template=template,
        parameters=parameters,
    )

    deployment_create_result = self.resource_client.deployments.create_or_update(
        self.group_name,
        deployment_name,
        deployment_params,
    )
    deployment_create_result = deployment_create_result.result()
    self.assertEqual(deployment_name, deployment_create_result.name)

    deployment_list_result = self.resource_client.deployments.list_by_resource_group(
        self.group_name,
        None,
    )
    deployment_list_result = list(deployment_list_result)
    self.assertEqual(len(deployment_list_result), 1)
    self.assertEqual(deployment_name, deployment_list_result[0].name)

    deployment_get_result = self.resource_client.deployments.get(
        self.group_name,
        deployment_name,
    )
    self.assertEqual(deployment_name, deployment_get_result.name)

    deployment_operations = list(self.resource_client.deployment_operations.list(
        self.group_name,
        deployment_name
    ))
    self.assertGreater(len(deployment_operations), 1)

    deployment_operation = deployment_operations[0]
    deployment_operation_get = self.resource_client.deployment_operations.get(
        self.group_name,
        deployment_name,
        deployment_operation.operation_id
    )
    self.assertEqual(deployment_operation_get.operation_id, deployment_operation.operation_id)

    # Should throw, since the deployment is done => cannot be cancelled
    with self.assertRaises(azure.common.exceptions.CloudError) as cm:
        self.resource_client.deployments.cancel(
            self.group_name,
            deployment_name
        )
    self.assertIn('cannot be cancelled', cm.exception.message)

    # Validate
    validation = self.resource_client.deployments.validate(
        self.group_name,
        deployment_name,
        {'mode': azure.mgmt.resource.resources.models.DeploymentMode.incremental}
    )
    self.assertTrue(hasattr(validation, 'properties'))

    # Export template
    export = self.resource_client.deployments.export_template(
        self.group_name,
        deployment_name
    )
    self.assertTrue(hasattr(export, 'template'))

    # Delete the template
    async_delete = self.resource_client.deployments.delete(
        self.group_name,
        deployment_name
    )


async_delete.wait()