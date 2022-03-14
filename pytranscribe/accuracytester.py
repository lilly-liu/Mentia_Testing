from accuracy import *
from get_transcription import *

actual_sentence = "An object relational mapper is a code library that automates the transfer of data stored in relational, databases into objects that are more commonly used in application code or EMS are useful because they provide a high level abstraction upon a relational database that allows developers to write Python code instead of sequel to create read update and delete, data and schemas in their database. Developers can use the programming language. They are comfortable with to work with a database instead of writing SQL "

input = printTrans()
if __name__ == "__main__":
    accuracyPrint(input, actual_sentence)
