from core.discord.bot import Bot


class DiscordSiteUtils:

    search = None

    def __init__(self, ctx):
        self.ctx = ctx

    def check(self, reaction, user) -> bool:
        matched_reaction = ""
        match len(self.search):
            case 1:
                matched_reaction = "0️⃣"
            case 2:
                matched_reaction = "0️⃣1️⃣"
            case 3:
                matched_reaction = "0️⃣1️⃣2️⃣"
            case 4:
                matched_reaction = "0️⃣1️⃣2️⃣3️⃣"
            case 5:
                matched_reaction = "0️⃣1️⃣2️⃣3️⃣4️⃣"

        return (
            user == self.ctx.author
            and self.ctx.message.id == reaction.message.id
            and str(reaction.emoji) in matched_reaction
        )

    async def prices(self, sku, bot: Bot, site_service, embed_builder_service):
        message = await self.ctx.send("Loading ⌛️")
        self.search = await site_service.search(sku=sku)
        if self.search:
            embed = await embed_builder_service.build_sneakers_embed(self.search)
            await message.edit(content="", embed=embed)
            reaction = ""
            for i, sneaker in enumerate(self.search):
                match i:
                    case 0:
                        reaction = "0️⃣"
                    case 1:
                        reaction = "1️⃣"
                    case 2:
                        reaction = "2️⃣"
                    case 3:
                        reaction = "3️⃣"
                    case 4:
                        reaction = "4️⃣"
                await message.add_reaction(reaction)

            # Await reaction
            reaction = await bot.slash_client._discord.wait_for(
                "reaction_add", check=self.check
            )

            # Prices embed
            await message.edit(content="Loading ⌛️", embed=None)
            await message.clear_reactions()
            sneaker, sneaker_prices = None, None
            match str(reaction[0]):
                case "0️⃣":
                    sneaker = self.search[0]
                case "1️⃣":
                    sneaker = self.search[1]
                case "2️⃣":
                    sneaker = self.search[2]
                case "3️⃣":
                    sneaker = self.search[3]
                case "4️⃣":
                    sneaker = self.search[4]
            sneaker_prices = await site_service.get_prices(sneaker)
            embed = await embed_builder_service.build_prices_embed(
                sneaker, sneaker_prices
            )
            await message.edit(content="", embed=embed)
        else:
            await message.edit(content="No sneaker found 😓")
