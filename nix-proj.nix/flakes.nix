{ config, pkgs, lib, ... }:

{
   nix.url = "";
   import = {
    ./defalut.nix
  };

  configuration.nixvim.enable = true;
  nixvim.config = {
    ./defalut.nix
  };
  ijadux2.nix.configuration = {
    home-manager.Packages = {
     pkgs.kitty
     pkgs.chromium
     pkgs.zsh
     pkgs.neovim
   };
  };
}
