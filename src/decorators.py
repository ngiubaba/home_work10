import  datetime

def log(filename=None):
    def log_function(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S")

            try:
                # start_message = f"{start_time} Функция {func.__name__} начала работу"
                result = func(*args, **kwargs)
                log_message = f"{start_time} {func.__name__} ok"
                buffer_result = result

            except Exception as e:
                error_message = str(e)
                log_message = (f"{start_time} Функция {func.__name__} error: {error_message}."
                               f" Inputs: ({args}, {kwargs})")
                # buffer_result = None

            if filename:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)
            return buffer_result
        return wrapper
    return log_function