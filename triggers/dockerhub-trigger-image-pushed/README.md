# dockerhub-trigger-image-pushed

This trigger fires when an image is pushed to the Docker Hub registry.

## Setup Instructions

**NOTE: You must be an administrator of the image repository that triggers the workflow"**

- Navigate to the repository you want to trigger 
- Click "Manage repository" > "Webhooks"
- Name your webhook (e.g. "relay")
- Navigate to your Relay workflow and copy the webhook url
- Paste it into the field "Webhook URL"
- Click "Create"
