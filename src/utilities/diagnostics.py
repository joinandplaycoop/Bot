import time
import functools
import inspect

def executionTime():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{args[0].__name__}.{func.__name__}(): {end - start}")
            return result
        return wrapper
    return decorator


def verboseError(func):
    """Decorator for generic server-based high permission test
    OnError, sends exception to chat
    """
    async def decorator(self, ctx,*args, **kwargs):        
         try:
            await func(self, ctx, *args, **kwargs)
         except Exception as e:
           await ctx.send(str(e))

    decorator.__name__ = func.__name__
    sig = inspect.signature(func)
    decorator.__signature__ = sig # sig.replace(parameters=tuple(sig.parameters.values())[1:]) # from ctx onward
    return decorator