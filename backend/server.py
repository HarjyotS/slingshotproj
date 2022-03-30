import flask
import trie

# create a flask app that allows the users to edit the trie


def main():
    # create a trie object
    trie_obj = trie.Trie()
    # create a flask app
    app = flask.Flask(__name__)
    # create a route for the root of the trie
    # @app.route("/")
    # def front_page():
    @app.route("/")
    def front_page():
        return flask.render_template("index.html")
    @app.route("/words")
    def words():
        # extract all the words in the trie
        words = trie_obj.extract_all()
        # create a string of all the words

        # return the string of all the words
        return {"words": words}, 200

    # create a route for adding a word to the trie
    @app.route("/add/<word>")
    def add(word):
        try:
            # check if word is not only letters
            if not word.isalpha():
                return {"Error": "Word must be only letters"}, 400

            # add the word to the trie
            trie_obj.add_keyword(word)
            # return the word
            return {"Status": "True"}, 200
        except Exception as e:
            return {"Error": str(e)}, 400

    # create a route for removing a word from the trie
    @app.route("/remove/<word>")
    def remove(word):
        try:
            # check if word is in trie
            if not trie_obj.search(word):
                return {"Error": "Word not in trie"}, 400
            # remove the word from the trie
            trie_obj.remove(word)
            # return the word
            return {"Status": "True"}, 200
        except Exception as e:
            return {"Error": str(e)}, 400

    @app.route("/search/<word>")
    def search(word):
        try:
            # search the trie for the word
            result = trie_obj.search(word)
            print(result)
            # return the result
            return {"Status": result}, 200
        except Exception as e:
            return {"Error": str(e)}, 400

    @app.route("/struct")
    def display():
        try:
            # display the trie structure
            return {"trie": (trie_obj.display_trie())}, 200
        except Exception as e:
            return {"Error": str(e)}, 400

    @app.route("/suggest/<prefix>")
    def sug(prefix):
        try:
            # search for suggestions with a given prefix
            suggestions = trie_obj.suggest(prefix)
            # return the suggestions
            return {"Status": suggestions}, 200
        except Exception as e:
            return {"Error": str(e)}, 400

    @app.route("/clear")
    def clear():
        # clear the trie
        trie_obj.clear_trie()
        # return the message
        return {"Status": "Trie cleared"}

    # error handeling for 404's
    @app.errorhandler(404)
    def page_not_found(e):
        return {"Error": "The requested endpoint is not found, 404."}, 404

    # run the app
    app.run()


main()

# #    # return the children of the trie recursivly in a dictionary
