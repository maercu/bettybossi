<template>
  <v-container class="fill-height">
    <v-responsive class="align-center fill-height">
      <v-table>
        <thead>
          <tr>
            <th class="text-left">
              First Name
            </th>
            <th class="text-left">
              Last Name
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in users">
            <td>{{ item.first_name }}</td>
            <td>{{ item.last_name }}</td>
          </tr>
        </tbody>
      </v-table>
    </v-responsive>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue';

  const users = ref(null);

  fetch('https://reqres.in/api/users')
      .then(response => response.json())
      .then(data => users.value = data.data);
  // let desserts = [
  //   {
  //     name: 'Frozen Yogurt',
  //     calories: 159,
  //   },
  //   {
  //     name: 'Ice cream sandwich',
  //     calories: 237,
  //   },
  //   {
  //     name: 'Eclair',
  //     calories: 262,
  //   },
  //   {
  //     name: 'Cupcake',
  //     calories: 305,
  //   },
  //   {
  //     name: 'Gingerbread',
  //     calories: 356,
  //   },
  //   {
  //     name: 'Jelly bean',
  //     calories: 375,
  //   },
  //   {
  //     name: 'Lollipop',
  //     calories: 392,
  //   },
  //   {
  //     name: 'Honeycomb',
  //     calories: 408,
  //   },
  //   {
  //     name: 'Donut',
  //     calories: 452,
  //   },
  //   {
  //     name: 'KitKat',
  //     calories: 518,
  //   }
  // ]
</script>
