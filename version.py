"""
Version tracking for Pokemon Monopoly shared components.

SHARED_VERSION: Incremented when protocol/enums change (breaking changes)
DATA_VERSION: Updated by the Pokemon scraper when data changes
DATA_POKEMON_COUNT: Number of Pokemon in current dataset
"""

SHARED_VERSION = "1.0.0"
DATA_VERSION = "2024.02-gen9"
DATA_POKEMON_COUNT = 1025
DATA_LAST_POKEMON = "Pecharunt"

def check_compatibility(client_version: str, server_version: str) -> tuple[bool, str]:
    """
    Check if client and server shared versions are compatible.
    
    Returns:
        Tuple of (is_compatible, message)
    """
    client_major = client_version.split(".")[0]
    server_major = server_version.split(".")[0]
    
    if client_major != server_major:
        return False, f"Major version mismatch: client={client_version}, server={server_version}"
    
    if client_version != server_version:
        return True, f"Minor version difference: client={client_version}, server={server_version}"
    
    return True, "Versions match"

