

import ollama

def generate_product_description(product_name, product_category, product_features):
    """
    Generate a professional and engaging product description using TinyLlama via Ollama.
    
    Args:
        product_name (str): The name of the product.
        product_category (str): The category it belongs to.
        product_features (str): Key features in comma-separated or paragraph form.

    Returns:
        str: Generated product description or an error message.
    """
    prompt = f"""
    Write a professional and engaging product description for the following:

    Product Name: {product_name}
    Category: {product_category}
    Key Features: {product_features}

    The description should be suitable for an online store listing, appealing to potential buyers.
    """

    try:
        # Call Ollama with the TinyLlama model
        response = ollama.chat(
            model="tinyllama",
            messages=[
                {"role": "user", "content": prompt.strip()}
            ]
        )

        # Extract generated content
        description = response.get("message", {}).get("content", "").strip()
        if not description:
            description = "No description generated. Please try again."
    except Exception as e:
        description = f"Error generating description: {str(e)}"

    return description
