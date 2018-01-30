import sys
from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage import CloudStorageAccount
from azure.storage.blob.models import ContentSettings, PublicAccess

credentials = UserPassCredentials('', '')
subscription_id = ''

resource_client = ResourceManagementClient(credentials, subscription_id)
storage_client = StorageManagementClient(credentials, subscription_id)

resource_group_name = 'Invivoo-elastic'
resource_client.resource_groups.create_or_update(
    resource_group_name,
    {
        'location':'westeurope'
    }
)

sys.exit(0)

storage_account_name = 'myuniquestorageaccount'
async_create = storage_client.storage_accounts.create(
    resource_group_name,
    storage_account_name,
    {
        'location':'westeurope',
        'kind':'storage',
        'sku': {
            'name':'standard_ragrs'
        }
    }
)
async_create.wait()

storage_keys = storage_client.storage_accounts.list_keys(resource_group_name, storage_account_name)
storage_keys = {v.key_name: v.value for v in storage_keys.keys}

storage_client = CloudStorageAccount(storage_account_name, storage_keys['key1'])

blob_service = storage_client.create_block_blob_service()

blob_service.create_container(
    'mycontainername',
    public_access=PublicAccess.Blob
)

blob_service.create_blob_from_bytes(
    'mycontainername',
    'myblobname',
    b'<center><h1>Hello World!</h1></center>',
    content_settings=ContentSettings('text/html')
)

print(blob_service.make_blob_url('mycontainername', 'myblobname'))