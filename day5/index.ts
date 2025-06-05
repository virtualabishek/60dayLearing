import { log } from "console";
import { PrismaClient } from "./generated/prismaprisma";
const prisma = new PrismaClient();

async function main() {
  //   Write
  await prisma.user.create({
    data: {
      name: "Abishek",
      email: "717abishek@gmail.com",
      posts: {
        create: { title: "Hello World", content: "Life is fun" },
      },
      profile: {
        create: { bio: "I like coding" },
      },
    },
  });
  // Read
  const allUsers = await prisma.user.findMany({
    include: {
      posts: true,
      profile: true,
    },
  });
  console.log(allUsers);

  // post
  async function main() {
    const post = await prisma.post.update({
      where: { id: 1 },
      data: { published: true },
    });
    console.log(post);
  }
}

main()
  .then(async () => {
    await prisma.$disconnect();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    process.exit(1);
  });
