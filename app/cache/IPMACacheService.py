
import time

cacheIPMA = {}


def search_in_cache(destrict, city):
    """
        Finds if there is a key pair value in cache
        Args:
            destrict (str): Destrict name
            city (str): City name

        Returns:
            bool: True if found in cache and within ttl false otherwise
        """
    key = f"{destrict.lower()}_{city.lower()}"
    for cached_key in cacheIPMA:
        if key == cached_key:
            if 'ttl' in cacheIPMA[cached_key]:
                if cacheIPMA[cached_key]['ttl'] > time.time() - 3600:  # 1 h de TTL
                    return True
                else:
                    cacheIPMA[cached_key] = {}
                    return False
            else:
                return False
    return False