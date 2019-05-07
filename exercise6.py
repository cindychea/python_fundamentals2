def wrap_text(message, wrapper):
    return wrapper + message + wrapper

print(wrap_text(wrap_text(wrap_text("Cindy", "###"), "==="), "---"))