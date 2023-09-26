" " "
write a function called linear_search_product that takes the list of products and a target products
name as input. thr function should perform a linear search to find the target product in the list and 
return a list of indices of all occurrence of the product if found, or an empty list if the product is not 
found. 
" " "


def linearsearchproduct(productlist, targetproduct):
    indices=[]

for index, product in enumerate(productlist):
    if product ==target product:
      indices. append (index)

return indices


#example usage:
product=["shoes","boot" ,"loafer","shoes","sandal","shoes" ]
target="shoes"
result=linearsearchproduct (product, target)
print (result)
