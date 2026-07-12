import random
import logging
import asyncio


logger = logging.getLogger(__name__)
def retry_with_backoff(exception = Exception, max_attempts: int =3,):

    def decorator(func):
        
        async def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                
                except exception as e:
        
                    base_delay = 2
                    multiplier = 3.0
                    max_delay = 30

                    print(f"Retrying: {i+1}/{max_attempts}")
                    intial_delay = base_delay * (multiplier ** i)
                    jitter = (random.uniform(0.5, 1.5)  * intial_delay)
                    cap = min(jitter, max_delay)
                    await asyncio.sleep(cap)

                    
                if (i==max_attempts-1):
                    raise Exception(f"\nAll retry attempts failed")  #exhaused all delays
                        
        return wrapper
    return decorator
    
                
                
# *args = positional arguments, **kwargs = keyword arguments. 
# They capture whatever arguments get passed to the wrapped function so you can forward them along.
