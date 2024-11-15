try:
    pass

except ValueError:
    pass

except (ZeroDivisionError, AssertionError):
    pass
# ...
except Exception as result:
    print(result)

# 当没有捕获到异常时执行的代码
else:
    pass

finally:
    print("不论出没出错都会执行的代码")
