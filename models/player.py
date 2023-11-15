from helpers.addresses import (
  GAME_BASE,
  PLAYER_BASE,
  PLAYER_NAME_OFFSET,
  PLAYER_CURRENT_HP_OFFSET,
  PLAYER_MAX_HP_OFFSET,
  PLAYER_COORDINATE_X_OFFSET,
  PLAYER_COORDINATE_Y_OFFSET,
  MAP_NAME_OFFSET,
  STATE_OFFSET
)


class Player():
  state_map = {
    0: "idle",
    1: "walking",
    2: "attacking",
    5: "looting",
    6: "sitting",
    7: "delay",
    9: "attacking"
  }

  def __init__(self, game, world_base):
    self.game = game
    self.base = self.game.process.memory.read_ptr(world_base, PLAYER_BASE)
    self.current_action = "idle"

  def name(self):
    return self.game.process.memory.read_str(GAME_BASE + PLAYER_NAME_OFFSET)

  def hp(self):
    return self.game.process.memory.read_u_int(GAME_BASE + PLAYER_CURRENT_HP_OFFSET)

  def max_hp(self):
    return self.game.process.memory.read_u_int(GAME_BASE + PLAYER_MAX_HP_OFFSET)

  def map_name(self):
    name = self.game.process.memory.read_str(GAME_BASE + MAP_NAME_OFFSET)

    if name:
      return name.split(".rsw")[0]

    return None

  def coordinates(self):
    return (self.game.process.memory.read_u_int(GAME_BASE + PLAYER_COORDINATE_X_OFFSET), self.game.process.memory.read_u_int(GAME_BASE + PLAYER_COORDINATE_Y_OFFSET))

  def state(self):
    return self.game.process.memory.read_u_int(self.base + STATE_OFFSET)
