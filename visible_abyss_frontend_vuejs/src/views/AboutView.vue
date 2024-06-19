<template>
  <div class="about">
    <h1>This is an about page</h1>

    <div class="inline-block m-2 rounded cursor-pointer shadow transition-all duration-150 ease-in-out transform hover:scale-105 ">
      <span class="bg-blue-500 text-white px-2 py-1 rounded-l">Search</span>
      <span class="bg-blue-700 text-white px-2 py-1 rounded-r font-bold">搜索</span>
    </div>

    <a-button type="dashed" status="danger" shape="round">Danger</a-button>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
