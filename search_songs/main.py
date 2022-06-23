from optparse import OptionParser

from requests.exceptions import ConnectionError, HTTPError

from search_songs.search import search

version = open('search_songs/version').read()


def main():
    usage = "usage: %prog [options] text"
    parser = OptionParser(usage)

    parser.add_option("-v", "--version",
                      action="store_true",
                      help="app version")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    if options.version:
        print(f'version == {version}')
    try:
        songs = search(*args)
    except ConnectionError:
        print('Error. Please, check your Internet connection')
    except HTTPError:
        print('Error. Try later')
    except:
        print('Unknown error')
    else:
        print(*songs, sep=',\n') if songs else print("Not founded")


if __name__ == "__main__":
    main()
