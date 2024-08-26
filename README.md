# Arcaflow OpenSearch

A plugin for loading data into an OpenSearch-compatible instance.

## Development

During the development of this plugin it is useful to start a local Elasticsearch via:
```bash
docker compose -f docker-compose-dev.yaml up -d
```

and stop it again via:
```bash
docker compose -f docker-compose-dev.yaml down -v
```

## Testing

The tests of this plugin are split up into `unit` and `integration` tests located in 
- [./tests/integration/](./tests/integration/)
- [./tests/unit/](./tests/unit/)

### Unit Tests

Run all unit tests via:
```bash
# Run all unit tests
python -m unittest tests.unit.test_opensearch_plugin
```

### Integration Tests

Running all integration tests can be run either 
- using a running a local Elasticsearch as described in [Development](#development) and then execute the tests via
```bash
# Run all integration tests
python -m unittest tests.integration.test_opensearch_plugin
```

- using the [docker-compose.yaml](./docker-compose.yaml) and run
```bash
# the --abort-on-container-exit ensures a `docker compose down` after the tests have run
docker compose -f docker-compose.yaml up --abort-on-container-exit
```

__Note:__ Make sure to `docker compose down` and remove the volume after one run as there is currently no cleanup done.

# Autogenerated Input/Output Documentation by Arcaflow-Docsgen Below

<!-- Autogenerated documentation by arcaflow-docsgen -->
## OpenSearch (`opensearch`)

Load data into opensearch compatible instance

### Input

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>DocumentRequest</td></tr>
<tr><th>Properties</th><td><details><summary>bulk_upload_list (<code>list[<code>reference[BulkUploadObject]</code>]</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>bulk upload list</td></tr><tr><th>Description:</th><td width="500">The list of objects for the bulk upload operation.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>list[<code>reference[BulkUploadObject]</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>List items</summary>
        <table><tbody><tr><th>Type:</th><td><code>reference[BulkUploadObject]</code></td><tr><th>Referenced object:</th><td>BulkUploadObject</td></tr></tbody></table>
    </details>
</td></tr></tbody></table>
            </details><details><summary>default_index (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>index</td></tr><tr><th>Description:</th><td width="500">Name of the default index that will receive the data.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Minimum length:</th><td>1</td></tr></tbody></table>
            </details><details><summary>metadata (<code>map[<code>string</code>,<code>any</code>]</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>metadata</td></tr><tr><th>Description:</th><td width="500">Optional global metadata object that will be added to every document.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>map[<code>string</code>,<code>any</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>Key type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
<tr><td colspan="2">
    <details>
        <summary>Value type</summary>
        <table><tbody><tr><th>Type:</th><td><code>any</code></td></tbody></table>
    </details>
</td></tr>
</tbody></table>
            </details><details><summary>password (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>password</td></tr><tr><th>Description:</th><td width="500">The password for the given user.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>tls_verify (<code>bool</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>TLS verify</td></tr><tr><th>Description:</th><td width="500">For development and testing purposes, this can be set to False to disable TLS verification for connections to Opensearch-compatible services.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Default (JSON encoded):</th><td><pre><code>true</code></pre></td></tr><tr><th>Type:</th><td><code>bool</code></td></tbody></table>
            </details><details><summary>url (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>url</td></tr><tr><th>Description:</th><td width="500">The URL for the Opensearch-compatible instance.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>username (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>username</td></tr><tr><th>Description:</th><td width="500">A username for an authorized user for the given Opensearch-compatible instance.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Minimum length:</th><td>1</td></tr></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>BulkUploadObject (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>data (<code>map[<code>string</code>,<code>any</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>data</td></tr><tr><th>Description:</th><td width="500">The JSON data document to upload to your index.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>map[<code>string</code>,<code>any</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>Key type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
<tr><td colspan="2">
    <details>
        <summary>Value type</summary>
        <table><tbody><tr><th>Type:</th><td><code>any</code></td></tbody></table>
    </details>
</td></tr>
</tbody></table>
        </details><details><summary>operation (<code>map[<code>string</code>,<code>reference[OperationMeta]</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>operation</td></tr><tr><th>Description:</th><td width="500">The operation type and associated operation metadata.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>map[<code>string</code>,<code>reference[OperationMeta]</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>Key type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
<tr><td colspan="2">
    <details>
        <summary>Value type</summary>
        <table><tbody><tr><th>Type:</th><td><code>reference[OperationMeta]</code></td><tr><th>Referenced object:</th><td>OperationMeta</td></tr></tbody></table>
    </details>
</td></tr>
</tbody></table>
        </details></td></tr>
</tbody></table>
        </details><details><summary>DocumentRequest (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>bulk_upload_list (<code>list[<code>reference[BulkUploadObject]</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>bulk upload list</td></tr><tr><th>Description:</th><td width="500">The list of objects for the bulk upload operation.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>list[<code>reference[BulkUploadObject]</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>List items</summary>
        <table><tbody><tr><th>Type:</th><td><code>reference[BulkUploadObject]</code></td><tr><th>Referenced object:</th><td>BulkUploadObject</td></tr></tbody></table>
    </details>
</td></tr></tbody></table>
        </details><details><summary>default_index (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>index</td></tr><tr><th>Description:</th><td width="500">Name of the default index that will receive the data.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Minimum length:</th><td>1</td></tr></tbody></table>
        </details><details><summary>metadata (<code>map[<code>string</code>,<code>any</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>metadata</td></tr><tr><th>Description:</th><td width="500">Optional global metadata object that will be added to every document.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>map[<code>string</code>,<code>any</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>Key type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
<tr><td colspan="2">
    <details>
        <summary>Value type</summary>
        <table><tbody><tr><th>Type:</th><td><code>any</code></td></tbody></table>
    </details>
</td></tr>
</tbody></table>
        </details><details><summary>password (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>password</td></tr><tr><th>Description:</th><td width="500">The password for the given user.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>tls_verify (<code>bool</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>TLS verify</td></tr><tr><th>Description:</th><td width="500">For development and testing purposes, this can be set to False to disable TLS verification for connections to Opensearch-compatible services.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Default (JSON encoded):</th><td><pre><code>true</code></pre></td></tr><tr><th>Type:</th><td><code>bool</code></td></tbody></table>
        </details><details><summary>url (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>url</td></tr><tr><th>Description:</th><td width="500">The URL for the Opensearch-compatible instance.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>username (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>username</td></tr><tr><th>Description:</th><td width="500">A username for an authorized user for the given Opensearch-compatible instance.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Minimum length:</th><td>1</td></tr></tbody></table>
        </details></td></tr>
</tbody></table>
        </details><details><summary>OperationMeta (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>_id (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ID</td></tr><tr><th>Description:</th><td width="500">Optional ID for the data document.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>_index (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>index</td></tr><tr><th>Description:</th><td width="500">Optional name of the index that will receive the data. If none is provided, the default index will be used.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>

### Outputs


#### error

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>ErrorOutput</td></tr>
<tr><th>Properties</th><td><details><summary>error (<code>string</code>)</summary>
                <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>ErrorOutput (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>error (<code>string</code>)</summary>
        <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>

#### success

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>SuccessOutput</td></tr>
<tr><th>Properties</th><td><details><summary>document_ids (<code>list[<code>string</code>]</code>)</summary>
                <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>list[<code>string</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>List items</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr></tbody></table>
            </details><details><summary>message (<code>string</code>)</summary>
                <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>SuccessOutput (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>document_ids (<code>list[<code>string</code>]</code>)</summary>
        <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>list[<code>string</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>List items</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr></tbody></table>
        </details><details><summary>message (<code>string</code>)</summary>
        <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>



## Process List (`process_list`)

Process list input into a bulk_upload_list

### Input

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>DataList</td></tr>
<tr><th>Properties</th><td><details><summary>data_list (<code>list[<code>any</code>]</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>data list</td></tr><tr><th>Description:</th><td width="500">List of data object to process into the bulk_upload_list.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>list[<code>any</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>List items</summary>
        <table><tbody><tr><th>Type:</th><td><code>any</code></td></tbody></table>
    </details>
</td></tr></tbody></table>
            </details><details><summary>operation (<code>map[<code>string</code>,<code>reference[OperationMeta]</code>]</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>operation</td></tr><tr><th>Description:</th><td width="500">The operation type and associated operation metadata.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>map[<code>string</code>,<code>reference[OperationMeta]</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>Key type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
<tr><td colspan="2">
    <details>
        <summary>Value type</summary>
        <table><tbody><tr><th>Type:</th><td><code>reference[OperationMeta]</code></td><tr><th>Referenced object:</th><td>OperationMeta</td></tr></tbody></table>
    </details>
</td></tr>
</tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>DataList (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>data_list (<code>list[<code>any</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>data list</td></tr><tr><th>Description:</th><td width="500">List of data object to process into the bulk_upload_list.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>list[<code>any</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>List items</summary>
        <table><tbody><tr><th>Type:</th><td><code>any</code></td></tbody></table>
    </details>
</td></tr></tbody></table>
        </details><details><summary>operation (<code>map[<code>string</code>,<code>reference[OperationMeta]</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>operation</td></tr><tr><th>Description:</th><td width="500">The operation type and associated operation metadata.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>map[<code>string</code>,<code>reference[OperationMeta]</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>Key type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
<tr><td colspan="2">
    <details>
        <summary>Value type</summary>
        <table><tbody><tr><th>Type:</th><td><code>reference[OperationMeta]</code></td><tr><th>Referenced object:</th><td>OperationMeta</td></tr></tbody></table>
    </details>
</td></tr>
</tbody></table>
        </details></td></tr>
</tbody></table>
        </details><details><summary>OperationMeta (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>_id (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ID</td></tr><tr><th>Description:</th><td width="500">Optional ID for the data document.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>_index (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>index</td></tr><tr><th>Description:</th><td width="500">Optional name of the index that will receive the data. If none is provided, the default index will be used.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>

### Outputs


#### error

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>ErrorOutput</td></tr>
<tr><th>Properties</th><td><details><summary>error (<code>string</code>)</summary>
                <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>ErrorOutput (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>error (<code>string</code>)</summary>
        <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>

#### success

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>BulkUploadList</td></tr>
<tr><th>Properties</th><td><details><summary>bulk_upload_list (<code>list[<code>reference[BulkUploadObject]</code>]</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>bulk upload list</td></tr><tr><th>Description:</th><td width="500">The list of objects for the bulk upload operation.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>list[<code>reference[BulkUploadObject]</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>List items</summary>
        <table><tbody><tr><th>Type:</th><td><code>reference[BulkUploadObject]</code></td><tr><th>Referenced object:</th><td>BulkUploadObject</td></tr></tbody></table>
    </details>
</td></tr></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>BulkUploadList (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>bulk_upload_list (<code>list[<code>reference[BulkUploadObject]</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>bulk upload list</td></tr><tr><th>Description:</th><td width="500">The list of objects for the bulk upload operation.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>list[<code>reference[BulkUploadObject]</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>List items</summary>
        <table><tbody><tr><th>Type:</th><td><code>reference[BulkUploadObject]</code></td><tr><th>Referenced object:</th><td>BulkUploadObject</td></tr></tbody></table>
    </details>
</td></tr></tbody></table>
        </details></td></tr>
</tbody></table>
        </details><details><summary>BulkUploadObject (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>data (<code>map[<code>string</code>,<code>any</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>data</td></tr><tr><th>Description:</th><td width="500">The JSON data document to upload to your index.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>map[<code>string</code>,<code>any</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>Key type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
<tr><td colspan="2">
    <details>
        <summary>Value type</summary>
        <table><tbody><tr><th>Type:</th><td><code>any</code></td></tbody></table>
    </details>
</td></tr>
</tbody></table>
        </details><details><summary>operation (<code>map[<code>string</code>,<code>reference[OperationMeta]</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>operation</td></tr><tr><th>Description:</th><td width="500">The operation type and associated operation metadata.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>map[<code>string</code>,<code>reference[OperationMeta]</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>Key type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
<tr><td colspan="2">
    <details>
        <summary>Value type</summary>
        <table><tbody><tr><th>Type:</th><td><code>reference[OperationMeta]</code></td><tr><th>Referenced object:</th><td>OperationMeta</td></tr></tbody></table>
    </details>
</td></tr>
</tbody></table>
        </details></td></tr>
</tbody></table>
        </details><details><summary>OperationMeta (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>_id (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ID</td></tr><tr><th>Description:</th><td width="500">Optional ID for the data document.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>_index (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>index</td></tr><tr><th>Description:</th><td width="500">Optional name of the index that will receive the data. If none is provided, the default index will be used.</td></tr><tr><th>Required:</th><td>No</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>
<!-- End of autogenerated documentation -->
