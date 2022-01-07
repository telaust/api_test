# API over HTTP – FastAPI

### Welltory task

## Usage

All responses will have the form

```shell
docker run python-docker
```

Subsequent response definitions will only detail the expected value of the `data field`

### Calculate metrics

**Definition**

`POST /calculate`

**Response**

- `200 OK` on success

```json
{
  "user_id": int,
  "data": {
    "x_data_type": str,
    "y_data_type": str,
    "x": [
      {
        "date": YYYY-MM-DD,
        "value": float,
      },
      ...
    ],
    "y": [
      {
        "date": YYYY-MM-DD,
        "value": float,
      },
      ...
    ]
  }
}
```

### Get metrics for specific user

**Definition**

`GET /correlation?x_data_type=str&y_data_type=str&user_id=int`

**Arguments**

- `"identifier":string` a globally unique identifier for this device
- `"name":string` a friendly name for this device
- `"device_type":string` the type of the device as understood by the client
- `"controller_gateway":string` the IP address of the device's controller

If a device with the given identifier already exists, the existing device will be overwritten.

**Response**

- `200 OK` on success

```json
{
  "user_id": int,
  "x_data_type": str,
  "y_data_type": str,
  "correlation": {
    "value": float,
    "p_value": float,
  }
}
```
