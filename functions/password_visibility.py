def view_pass(pass_entry, eye_button, hide_pass):
    """Toggle to show the password."""
    hide_pass.config(file='Image/view.png')
    pass_entry.config(show='')
    eye_button.config(command=lambda: hide_pass_func(pass_entry, eye_button, hide_pass))

def hide_pass_func(pass_entry, eye_button, hide_pass):
    """Toggle to hide the password."""
    hide_pass.config(file='Image/hide.png')
    pass_entry.config(show='*')
    eye_button.config(command=lambda: view_pass(pass_entry, eye_button, hide_pass))
