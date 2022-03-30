# Trie Docs

## Server

To run the server simply install *flask*, you can do this by running `pip install flask`.
After installing flask open the directory the server is located in and run it using `python server.py`.

This will run the server on localhost on port 5000.

## Client

To run the client first install the requirements `pip install -r requirements.txt`
After this run `python client.py`. The client is built in a very easy to use way that asks for what you want to do in a forever loop. This allows you to issue multiple instructions without rerunning the client script.

## Api Docs
All api endpoints on this program can be used by simple **get** requests.

#### This Page

`https://trieapi.harjyotsahni.com/`

#### Adding a Word
`https://trieapi.harjyotsahni.com/add/<word>`
The api accepts all lowercase alpha words.
The api will return errors in index `Error` and this can be used for other clients and error handling.

#### Removing a Word
`https://trieapi.harjyotsahni.com/remove/<word>`
The api will remove the word that you enter if it is in the trie.
The api will return errors in index `Error` and this can be used for other clients and error handling.

#### Searching for a Word
`https://trieapi.harjyotsahni.com/search/<word>`
The api will seach for a word. The api will then return a true or false boolean.

#### Prefix Searches
`https://trieapi.harjyotsahni.com/suggest/<word>`
The api will search for words starting with the prefix you provide and return them in the form of a list.

#### Structure
`https://trieapi.harjyotsahni.com/struct`
The api will return the structure of the trie in a dictionary that clearly shows the links between parents and children.
#### Words
`https://trieapi.harjyotsahni.com/words`
The api will return all the words in the trie stored in a list.
#### Clear
`https://trieapi.harjyotsahni.com/clear`
The api will clear out all the contents of the trie.
