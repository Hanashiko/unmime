# unmime.py

This Python script decodes MIME quoted-printable encoded content from a file named `test.html` and prints the decoded output to the console.

## Usage

1.  Make sure you have Python installed on your system.
2.  Save the provided Python code as `unmime.py` in your Git repository.
3.  Create a file named `test.html` in the same directory as `unmime.py`.
4.  Place the MIME quoted-printable encoded content that you want to decode inside `test.html`.
5.  Open your terminal or command prompt, navigate to the directory containing `unmime.py`, and run the script using the following command:

    ```bash
    python unmime.py
    ```

6.  The decoded content from `test.html` will be printed to your terminal.

## Functionality

The script performs the following steps:

1.  **Imports the `quopri` module:** This module provides functions for encoding and decoding MIME quoted-printable data.
2.  **Opens and reads `test.html`:** It opens the file named `test.html` in read mode (`'r'`) and reads its entire content into the `encoded_content` variable.
3.  **Decodes the content:** It uses the `quopri.decodestring()` function to decode the quoted-printable encoded content stored in `encoded_content`. The result is a bytes object.
4.  **Decodes to UTF-8:** The decoded bytes object is then decoded into a Unicode string using the UTF-8 encoding.
5.  **Prints the decoded content:** Finally, the decoded string is printed to the standard output (your terminal).

## Example `test.html`

Input

    ```html
    =3D=3DThis is a line of text.=0D=0AAnd this is another line.=
    ```
Output

Running python unmime.py with the above test.html would produce the following output:

    ```html
    ==This is a line of text.
    And this is another line.
    ```
