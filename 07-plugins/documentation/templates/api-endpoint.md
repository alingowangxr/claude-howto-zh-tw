# [METHOD] /api/v1/[endpoint]

## Description

簡要說明這個 endpoint 的作用。

## Authentication

說明鑑權方式，例如 Bearer token。

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | Resource ID |

### Query Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| page | integer | No | Page number |
| limit | integer | No | Items per page |

### Request Body

```json
{
  "field": "value"
}
```

## Responses

### 200 OK

```json
{
  "success": true,
  "data": {
    "id": "123",
    "name": "Example"
  }
}
```

## Examples

### cURL

```bash
curl -X GET "https://api.example.com/api/v1/endpoint" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json"
```
