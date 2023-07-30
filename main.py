from mcpi.minecraft import Minecraft

mc = Minecraft.create(address="186.125.41.155", port=25565)
mc.postToChat("hola")
# print(mc.getPlayerEntityId("Thejairex"))