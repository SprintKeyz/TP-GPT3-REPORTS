# files are as follows: name, path

sentiment_file = ["", ""]
examples_file = ["", ""]

# handle the form submission
# takes two params: (request.POST, request.FILES)
# POST is a dictionary of form data
# FILES is a dictionary of files


def handle_submit(request, files):
    global final_path
    global sentiment_file
    global examples_file

    final_path = request.get('file-path')
    raw_sent_file = files.get('sentiment-file')
    raw_ex_file = files.get('examples-file')

    sentiment_file[0] = raw_sent_file
    examples_file[0] = raw_ex_file

    try:
        for line in raw_sent_file:
            sentiment_file[1] += line.decode('utf-8')

    except Exception as e:
        print("Error in sentiment file:", e)

    try:
        for line in raw_ex_file:
            examples_file[1] += line.decode('utf-8')

    except Exception as e:
        print("Error in examples file:", e)

    print_form_info()


def print_form_info():
    print("File path is", final_path)
    print("Sentiment file content (", sentiment_file[0], ")")
    print("--------")
    print(sentiment_file[1])
    print("--------")
    print("Examples file content (", examples_file[0], ")")
    print("--------")
    print(examples_file[1])
    print("--------")
