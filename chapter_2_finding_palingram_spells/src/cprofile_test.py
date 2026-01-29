import cProfile
import palingrams
import load_dictionary

word_list = load_dictionary.load("words")

cProfile.run('palingrams.find_palingrams(word_list)')
