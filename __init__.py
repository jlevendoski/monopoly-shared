"""
Shared module for Pokemon Monopoly.

Contains constants, enums, and protocol definitions used by
both the client and server.
"""

from shared.constants import (
    BOARD_SIZE,
    STARTING_MONEY,
    SALARY_AMOUNT,
    JAIL_POSITION,
    GO_TO_JAIL_POSITION,
    JAIL_BAIL,
    MAX_JAIL_TURNS,
    PROPERTY_GROUPS,
    BOARD_SPACES,
)

from shared.enums import (
    SpaceType,
    PropertyGroup,
    GamePhase,
    PlayerState,
    CardType,
    TradeStatus,
    MessageType,
)

from shared.protocol import (
    Message,
    ErrorMessage,
    GameSettings,
    parse_message,
)

from shared.pokemon import (
    PokemonInfo,
    ItemInfo,
    PokemonDatabase,
    ItemDatabase,
    get_pokemon_database,
    get_item_database,
    generate_pokemon_assignments,
    generate_item_assignments,
)

from shared.version import (
    SHARED_VERSION,
    DATA_VERSION,
    DATA_POKEMON_COUNT,
    check_compatibility,
)
