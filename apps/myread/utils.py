from apps.core.constants import BOOK_CATEGORY

def generate_book_cat_list(book_per_cat):
    result = ''
    for item in book_per_cat:
        result += f'''
            <li>{BOOK_CATEGORY.get(item["category"]).capitalize()}: {item["cnt"]}</li>
        '''
    return result
