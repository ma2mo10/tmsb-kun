import discord
from discord.ext import commands
import sys
import os
import json

bot = commands.Bot(command_prefix="/")

#各種設定の読み込み
with open("settings") as file:
    token = file.readline().strip()
    gen1 = file.readline().strip()
    gen2 = file.readline().strip()
    gen3 = file.readline().strip()
    gen4 = file.readline().strip()
    gen5 = file.readline().strip()
    gen6 = file.readline().strip()
    gen7 = file.readline().strip()
    gen8 = file.readline().strip()


#データファイルの読み込みと結合
f = open(os.path.dirname(os.path.abspath(__file__))+gen1, "r", encoding="utf-8")
pokelist = json.load(f)
f = open(os.path.dirname(os.path.abspath(__file__))+gen2, "r", encoding="utf-8")
tmp = json.load(f)
pokelist.extend(tmp)
f = open(os.path.dirname(os.path.abspath(__file__))+gen3, "r", encoding="utf-8")
tmp = json.load(f)
pokelist.extend(tmp)
f = open(os.path.dirname(os.path.abspath(__file__))+gen4, "r", encoding="utf-8")
tmp = json.load(f)
pokelist.extend(tmp)
f = open(os.path.dirname(os.path.abspath(__file__))+gen5, "r", encoding="utf-8")
tmp = json.load(f)
pokelist.extend(tmp)
f = open(os.path.dirname(os.path.abspath(__file__))+gen6, "r", encoding="utf-8")
tmp = json.load(f)
pokelist.extend(tmp)
f = open(os.path.dirname(os.path.abspath(__file__))+gen7, "r", encoding="utf-8")
tmp = json.load(f)
pokelist.extend(tmp)
f = open(os.path.dirname(os.path.abspath(__file__))+gen8, "r", encoding="utf-8")
tmp = json.load(f)
pokelist.extend(tmp)



@bot.command(name="stats")
async def stats_get(ctx, pokename):
    
    #リクエストされたポケモンの情報の抽出
    pokemon = [x for x in pokelist if x['name'] == pokename]
    #ポケモンが存在しない場合の処理
    if len(pokemon)==0:
        await ctx.send("ポケモンが見つかりません")
        return

    types = pokemon[0]['types']
    hp, a, b, c, d, s, total = pokemon[0]['base_stats']
    abilities = pokemon[0]['abilities']

    #最速・準速・最遅の計算
    semi_s = s + 52
    top_s = int(semi_s * 1.1)
    worst_s = int(s * 0.9)
    top_s_scarf = int(top_s * 1.5)
    semi_s_scarf = int(semi_s * 1.5)



    #タイプ・特性を取り出す
    if len(types) == 2:
        type1 = types[0]
        type2 = types[1]
    else:
        type1 = types[0]
        type2 = "なし"

    if abilities[0] == abilities[1] and abilities[0] == abilities[2]:
        ability1 = abilities[0]
        ability2 = "なし"
        ability3 = "なし"
    elif abilities[0] == abilities[1] and abilities[0] != abilities[2]:
        ability1 = abilities[0]
        ability2 = "なし"
        ability3 = abilities[2]
    else:
        ability1 = abilities[0]
        ability2 = abilities[1]
        ability3 = abilities[2]
    

    #discordにデータを送信
    embed = discord.Embed(title="名前" ,description=pokename, color=0xff0000)
    embed.add_field(name="タイプ1",value=type1,inline=True)
    embed.add_field(name="タイプ2",value=type2,inline=True)
    embed.add_field(name="特性1",value=ability1,inline=False)
    embed.add_field(name="特性２",value=ability2,inline=False)
    embed.add_field(name="隠れ特性",value=ability3,inline=False)
    embed.add_field(name="HP",value=hp,inline=True)
    embed.add_field(name="攻撃",value=a,inline=True)
    embed.add_field(name="防御",value=b,inline=True)
    embed.add_field(name="特攻",value=c,inline=True)
    embed.add_field(name="特防",value=d,inline=True)
    embed.add_field(name="素早さ",value=s,inline=True)
    embed.add_field(name="合計",value=total,inline=False)
    embed.add_field(name="最速",value=top_s,inline=True)
    embed.add_field(name="準速",value=semi_s,inline=True)
    embed.add_field(name="最遅",value=worst_s,inline=True)
    embed.add_field(name="最速(スカーフ)",value=top_s_scarf,inline=True)
    embed.add_field(name="準速(スカーフ)",value=semi_s_scarf,inline=True)

    await ctx.send(embed=embed)



@bot.command(name="search")
async def search_stats(ctx, stat, param):
    stat_index = 0
    pokename_list = []

    #indexを決定
    if stat == "hp":
        stat_index = 0
    elif stat == "a":
        stat_index = 1
    elif stat == "b":
        stat_index = 2
    elif stat == "c":
        stat_index = 3
    elif stat == "d":
        stat_index = 4
    elif stat == "s":
        stat_index = 5
    else:
        await ctx.send("無効なコマンドです")
        return

    for x in pokelist:
        if x['base_stats'][stat_index] == int(param):
            pokename_list.append(x['name'])
        

    
    pokestr = stat+"種族値"+ param + "のポケモン\n"

    #discordにデータ送信
    pokename_list = '\n'.join(pokename_list)
    embed = discord.Embed(title=pokestr, description=pokename_list, color=0x00bfff)



    await ctx.send(embed=embed)
    



bot.run(token)