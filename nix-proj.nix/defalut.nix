{ config, pkgs, ... }:

{
  programs.kitty = {
    enable = true;
    theme = "catppuccin-mocha";
    font-family = "JetBrains Mono";
    font-size = "18";
    comfirm-os-close;
    tab-size = "2";
    #etc
  };
  programs.chromium.enable = true;
  
  programs.zsh = {
    enable = true;
          OhMyZsh = {
      enable = true;
      theme = "mh";
      plugins = [ "git" "sudo" "zoxide" "zsh-syntaxhighlighting"];
    };
     ShellAliasses = {
      cd = "z";
      ls = "lsd";
      lt = "ls --tree";
      x = "clear";
    };
    PROMPT = "%B%F{green}[%n@Nix-devops:%~]$ %f%b";
  };
  

  programs.home-manager = {
    enable = true;
    home.Packages = with pkgs; [
      kitty
      zsh
      chromium
    ];

  };
}
