I made the following commits to the repository:

1. Applied dictionary comprehension to `user_prompts` to convert keys to lowercase
2. Used `os.environ.get()` instead of `load_dotenv()` to access environment variables
3. Moved BOT_TOKEN existence check inside the `ChatBot` class initialization
4. Applied `@ staticmethod` decorator to the `main()` function
5. Removed unnecessary `if __name__ == "__main__": ` check and directly called `ChatBot.main()`

I have successfully optimized the Python script.
