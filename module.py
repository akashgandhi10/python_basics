import hello_module

hello_module.hello_func("akash")

from hello_module import hello_func

hello_func("gandhi")

import cal_module

print cal_module.cal(10, 2)

from cal_module import cal

print cal_module.cal(10, 2)


import package_module

package_module.hello_func("akash")
print package_module.cal(10, 2)
