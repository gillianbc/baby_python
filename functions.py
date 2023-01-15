def greet_user():
    """Display a simple greeting."""
    print("Hello!")

def make_tee_shirt(size=12, message='My sister bought me this shirt'):
    """Make a t-shirt"""
    txt = f'My t-shirt is size {size} with message {message}'
    print(txt)

def get_formatted_name(first, last):
    """Generate a title cased name"""
    fullname = f"{first} {last}"
    return fullname.title()

