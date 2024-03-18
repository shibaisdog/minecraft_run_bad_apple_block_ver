package org.source.shibaplugin;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.plugin.java.JavaPlugin;

public final class Shiba_Plugin extends JavaPlugin {
    private int x = -128;
    private int y = 120;
    private int z = -151;
    private int fr = 0;
    private World world;

    @Override
    public void onEnable() {
        world = Bukkit.getWorld("world");
        if (world == null) {
            getLogger().severe("Failed to get world!");
            return;
        }

        Bukkit.getScheduler().runTaskTimerAsynchronously(this, () -> {
            if (Bukkit.getOnlinePlayers().isEmpty() || fr >= 6572) {
                return;
            }
            try {
                URL url = new URL("http://localhost:3000/api/frame/" + fr);
                fr += 3;
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("GET");
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        updateBlocks(line);
                    }
                }
                connection.disconnect();
                y = 120;
            } catch (MalformedURLException malformedURLException) {
                getLogger().warning("Malformed URL: " + malformedURLException.getMessage());
            } catch (IOException ioException) {
                getLogger().warning("IO Exception: " + ioException.getMessage());
            }
        }, 0, 2);
    }
    private void updateBlocks(String line) {
        char[] letters = line.toCharArray();
        for (char letter : letters) {
            Location blockLocation = new Location(world, x, y, z);
            Material material = (letter == ' ') ? Material.BLACK_WOOL : Material.WHITE_WOOL;
            Bukkit.getScheduler().runTask(this, () -> {
                world.getBlockAt(blockLocation).setType(Material.AIR);
                world.getBlockAt(blockLocation).setType(material);
            });
            x--;
        }
        y--;
        x = -128;
    }
    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }
}