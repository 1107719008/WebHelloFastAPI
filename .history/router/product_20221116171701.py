from fastapi import APIRouter
from db.productJson import product_list

router = APIRouter( 
    prefix='/api/v1/products',   #後面的url可以少打/products
    tags=['products']
)


@router.get('/')
def get_all_products():
    # return products
    return product_list


@router.get('/id/{product_id}')
def get_product_by_id(product_id):
    return next((product for product in product_list if product['id'] == product_id))


@router.get("/{category}")
def get_product_by_category(category):
    category_list = []
    for product in product_list:
        if product['category'].upper() == category.upper():
            category_list.append(product)
    return category_list

@router.get("/{homework}")
def get_homework(hw):
    homework_list = []
    for hw in homework_list:
        if hw['new'].upper() == hw.upper():
            homework_list.append(hw)
    return homework_list

