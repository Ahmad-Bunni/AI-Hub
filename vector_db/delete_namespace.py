import pinecone

# Configuration
# Replace with your Pinecone API key
api_key = ""
# Replace with your Pinecone environment (e.g., 'us-west1-gcp')
environment = "northamerica-northeast1-gcp"
# Replace with the namespace you want to delete
namespace = ""

# Initialize Pinecone
pinecone.init(api_key=api_key, environment=environment)

index = pinecone.Index("default")

index.delete(delete_all=True, namespace=namespace)

print(f"Namespace '{namespace}' has been deleted.")
