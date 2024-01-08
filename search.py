from tabulate import tabulate
from vector_db import VectorDB


if __name__ == '__main__':
    index_path = 'db'        
    k_results = 5
    vector_db = VectorDB()
    vector_db.load_index(index_path)
    
    quit = False
    while not quit: 
        text = input('Type the text to search (or "q" to exit):')
        if text == 'q':
            quit = True
        else:
            results = vector_db.search(text, k_results)
            print('Showing {} top results:'.format(k_results))
            print(tabulate(results, headers=list(results.columns.values),
                           tablefmt = 'grid', maxcolwidths=40))

    